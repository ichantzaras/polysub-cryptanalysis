def get_blocks(text, size):
    blocks = [text[i:i+size] for i in range(0, len(text)-size, size)]
    return blocks


def get_columns(text_blocks):
    group_size = len(text_blocks[0])
    columns = []
    for letter_count in range(group_size):
        column = ''
        for group_count in range(len(text_blocks)):
            column += text_blocks[group_count][letter_count]
        columns.append(column)
    return columns


def to_blocks(cols):
    col_size = len(cols[0])
    blocks = []
    for letter in range(col_size):
        block = ''
        for col in range(len(cols)):
            block += cols[col][letter]
        blocks.append(block)
    return blocks

