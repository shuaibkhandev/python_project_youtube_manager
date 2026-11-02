import json

file_name = "youtube.txt"

def load_videos():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_videos(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)

def list_of_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")
    print("*"*70)
    print("\n")

def upload_video(videos):
    name = input("Enter the name of the video to upload: ")
    time = input("Enter the time of the video to upload: ")
    videos.append({"name": name, "time": time})
    save_videos(videos)
    print("Video has been uploaded successfully. \n")

def delete_video(videos):
    print("Video has been deleted successfully. \n")

def update_video(videos):
    print("Video has been updated successfully. \n")

def main():

    videos = load_videos()
    while True:
        print("Youtube Manager | Select an option")
        print("1. View Video List")
        print("2. Upload Video")
        print("3. Delete Video")
        print("4. Update Video")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case "1":
                list_of_videos(videos)
            case "2":
                upload_video(videos)
            case "3":
                delete_video(videos)    
            case "4":
                update_video(videos)
            case "5":
                print("Exiting the YouTube Manager. Goodbye! \n")
                break
            case _:
                print("Invalid choice. Please select a valid option (1-5). \n")



if __name__ == "__main__":
    main()


