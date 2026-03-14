class TranspositionCipher:
    def encrypt(self, text, key):
        # Create a list of empty strings for each column
        ciphertext = [''] * key

        # Loop through each column in ciphertext
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key

        # Convert list into a single string
        return ''.join(ciphertext)

    def decrypt(self, text, key):
        # Calculate number of columns and rows
        num_cols = int(len(text) / key)
        num_rows = key
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        # Each string in plaintext represents a column
        plaintext = [''] * num_cols

        col = 0
        row = 0
        for symbol in text:
            plaintext[col] += symbol
            col += 1

            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(plaintext)