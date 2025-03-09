using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace LinkDataTool
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("LINKDATA Files Encryption/Decryption Tool");
            Console.WriteLine("----------------------------------------");

            try
            {
                // Obter caminho da pasta
                Console.Write("Type the folder where the files are (ex.: 0.bin, 1.bin): ");
                string folderPath = Console.ReadLine();

                if (!Directory.Exists(folderPath))
                {
                    Console.WriteLine("Error: Not found!");
                    return;
                }

                // Escolher operação
                Console.Write("Type 'e' para encrypt or 'd' to decrypt: ");
                string operation = Console.ReadLine().ToLower();

                if (operation != "e" && operation != "d")
                {
                    Console.WriteLine("Error: Invalid operation! Use 'e' or 'd'");
                    return;
                }

                // Listar arquivos na pasta com padrão numérico (ex.: 0.bin, 1.bin)
                var files = Directory.GetFiles(folderPath)
                    .Where(f => Regex.IsMatch(Path.GetFileName(f), @"^\d+\.bin$"))
                    .ToArray();

                if (files.Length == 0)
                {
                    Console.WriteLine("Error: No valid files (ex.: 0.bin, 1.bin) found!");
                    return;
                }

                Console.WriteLine($"{files.Length} found files to process...");

                // Processar cada arquivo
                foreach (string filePath in files)
                {
                    string fileName = Path.GetFileNameWithoutExtension(filePath);
                    if (!uint.TryParse(fileName, out uint id))
                    {
                        Console.WriteLine($"Warning: Skipping {filePath} - Invalid name!");
                        continue;
                    }

                    byte[] data = File.ReadAllBytes(filePath);
                    Span<byte> dataSpan = data.AsSpan();

                    if (operation == "e")
                    {
                        LinkEncryption.Encrypt(dataSpan, id);
                        string outputPath = Path.Combine(folderPath, $"{fileName}.bin"); // Substitui o original
                        File.WriteAllBytes(outputPath, data);
                        Console.WriteLine($"Encrypted: {filePath} -> {outputPath} (ID: {id})");
                    }
                    else // "d"
                    {
                        LinkEncryption.Decrypt(dataSpan, id);
                        string outputPath = Path.Combine(folderPath, $"{fileName}.struct"); // Usa .struct
                        File.WriteAllBytes(outputPath, data);
                        Console.WriteLine($"Decrypted: {filePath} -> {outputPath} (ID: {id})");
                    }
                }

                Console.WriteLine("Done!");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }

    public static class LinkEncryption
    {
        public static void Encrypt(Span<byte> data, uint id)
            => Decrypt(data, id); // A encriptação é idêntica à decriptação (XOR simétrico)

        public static void Decrypt(Span<byte> data, uint id)
        {
            var gen = new Mersenne(id + 0x7F6BA458);
            var size = data.Length;

            for (var i = 0; i < size; i++)
            {
                var shift = (size - i >= 2) && (gen.Next() & 1) != 0 ? 1 : 0;
                var r = gen.Next();

                data[i] ^= (byte)r;
                if (i + shift < size)
                    data[i + shift] ^= (byte)(r >> 8);
                i += shift;
            }
        }
    }

    public class Mersenne
    {
        readonly uint[] State = new uint[4];

        public Mersenne(uint seed)
        {
            Init(seed);
        }

        public void Init(uint seed)
        {
            State[0] = 0x6C078965 * (seed ^ (seed >> 30));
            for (int i = 1; i < 4; i++)
                State[i] = (uint)(0x6C078965 * (State[i - 1] ^ (State[i - 1] >> 30)) + i);
        }

        public uint Next()
        {
            var temp = State[0] ^ (State[0] << 11);
            State[0] = State[1];
            State[1] = State[2];
            State[2] = State[3];
            State[3] ^= temp ^ ((temp ^ (State[3] >> 11)) >> 8);
            return State[3];
        }
    }
}