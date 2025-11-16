import json

DATA_FILE = 'youtube.txt'

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            test = json.load(file)
            print(test)
            return test 
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(DATA_FILE, 'w') as file:
        json.dump(videos, file)
    

def list_all_videos(videos):
    print("\n")
    print("*" * 70  )

    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}, video time: {video['time']}")
        
    print("\n")
    print("*" * 70  )


def add_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({"title": name, "time": time})
    save_data_helper(videos)
    print("Video added.\n")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: ")) 
    if 1 <= index <= len(videos):
        name = input("Enter new video title: ")
        time = input("Enter new video time: ")
        videos[index - 1] = {"title": name, "time": time}
        save_data_helper(videos)
        print("Video updated.\n")
    else:
        print("Invalid index!\n")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("Video deleted.\n")
    else:
        print("Invalid index!\n")    

  

def main():
    videos = load_data()
    while True:
        print("WELCOME TO THE YOUTUBE MANAGER || choose an option 📺")
        print("1. List all youtube videos📃")
        print("2. Add a new youtube video➕")
        print("3. update youtube video details")
        print("4. Delete a youtube video❌")
        print("5. Exit the YouTube Manager🚪")
        print(videos)

        choice = input("Enter your choice (1-5): ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice! Please choose a valid option.\n")

if __name__ == "__main__":
    main()
