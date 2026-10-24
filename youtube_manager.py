# file = open("youtube.txt", "w")

# try:
#     file.write("This is a sample text for YouTube manager.")
# finally:
#     file.close()


with open("youtube.txt", "w") as file:
    file.write("This is a sample text for YouTube manager.")