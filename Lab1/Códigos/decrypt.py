import sys
from scapy.all import rdpcap
from collections import Counter
from termcolor import colored

# Function to decrypt a message using Caesar cipher
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) - shift
            if shifted < ord('a'):
                shifted += 26
            decrypted_text += chr(shifted).upper() if is_upper else chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Function to calculate letter frequencies in a text
def letter_frequencies(text):
    text = text.lower()
    letter_count = Counter(text)
    total_letters = len(text)
    frequencies = {char: count / total_letters for char, count in letter_count.items()}
    return frequencies

# Function to find the most probable message in Spanish based on letter frequencies
def most_probable_message(decrypted_messages):
    spanish_letter_frequencies = {
        'a': 0.1253, 'b': 0.0142, 'c': 0.0468, 'd': 0.0586, 'e': 0.1368, 'f': 0.0069,
        'g': 0.0101, 'h': 0.0070, 'i': 0.0625, 'j': 0.0044, 'k': 0.0002, 'l': 0.0497,
        'm': 0.0315, 'n': 0.0671, 'o': 0.0868, 'p': 0.0251, 'q': 0.0088, 'r': 0.0687,
        's': 0.0798, 't': 0.0463, 'u': 0.0393, 'v': 0.0090, 'w': 0.0001, 'x': 0.0022,
        'y': 0.0090, 'z': 0.0052,
    }

    best_message = ""
    best_score = float('-inf')

    for decrypted_message in decrypted_messages:
        decrypted_message = decrypted_message.lower()
        freqs = letter_frequencies(decrypted_message)
        score = sum(spanish_letter_frequencies.get(char, 0) * freqs[char] for char in freqs)
        if score > best_score:
            best_score = score
            best_message = decrypted_message

    return best_message

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt_icmp.py <pcapng_file>")
        sys.exit(1)

    pcapng_file = sys.argv[1]

    try:
        packets = rdpcap(pcapng_file)
    except Exception as e:
        print(f"Error reading pcapng file: {str(e)}")
        sys.exit(1)

    icmp_type_8_packets = [packet for packet in packets if packet.haslayer("ICMP") and packet["ICMP"].type == 8]
    extracted_bytes = [packet.load[10:11].decode('utf-8', errors='ignore') for packet in icmp_type_8_packets]

    decrypted_messages = []
    for shift in range(1, 27):
        decrypted_messages.append(caesar_decrypt("".join(extracted_bytes), shift))

    for shift, decrypted_message in enumerate(decrypted_messages, start=1):
        print(f"Shift {shift}: {decrypted_message}")

    best_message = most_probable_message(decrypted_messages)
    print(colored(f"Most probable message in Spanish: {best_message}", 'green'))

if __name__ == "__main__":
    main()
