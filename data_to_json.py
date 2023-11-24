file_path = "data/goodreads_reviews_dedup.json"
dest_path = "data/test.json"
lines_number = 90000

with open(file_path) as input_file:
    head = [next(input_file) for _ in range(lines_number)]

with open(dest_path, 'w') as output_file:
    output_file.writelines('['+','.join(head)+']')
