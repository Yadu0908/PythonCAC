import json

def load_data():

    try:

        with open ("youtube.txt", 'r') as fileData:
            test = json.load(fileData)      #reads the data
            return test
        
    except FileNotFoundError:

        return []


def save_data_helper(videos):

    with open ("youtube.txt", 'w') as fileData:

        json.dump(videos, fileData)         #write's the data
    


def list_all_videos(videos):

    print("\n")
    print("****" * 15)
    for index, video in enumerate(videos, start= 1):

        print(f"{index}. {video['name']} - {video['time']} \n")

    print("\n")
    print("****" * 15)
    


def add_video(videos):

    name= input("Enter video name: ")
    time= input("Enter video time: ")
    
    videos.append({'name': name, 'time': time})     #bc we wanted to handle the data with JSON
    print(f"Video is added to the database successfully.\n")
    save_data_helper(videos)
    

def update_video(videos):

    list_all_videos(videos)

    index= int(input("Enter the video number to be update: "))

    if 1<= index <= len(videos):

        name= input("Enter the new video name: ")
        time= input("Enter the new video time: ")

        videos[index - 1] = {'name': name, 'time': time}
        print(f"Video number {videos[index-1]} is updated successfully.\n")

        save_data_helper(videos)

    else:

        print("Invalid index selected: ")

def delete_video(videos):

    list_all_videos(videos)
    index= int(input("Enter the video number to be deleted: "))


    if 1<= index <= len(videos):

        deleted_video_name =  videos[index-1]

        del videos[index-1]

        print(f"Video name {deleted_video_name['name']} is deleted successfully.\n")

        save_data_helper(videos)

    else:

        print("Invalid index selected: ")



def main():
    
    videos= load_data()

    while True:

        print("Youtube Manager| Choose an option.\n")

        print("1. List all fev video.\n")
        print("2. Add the youtube video.\n")
        print("3. Update a youtube video details.\n")
        print("4. Delete a youtube video.\n")
        print("5. Exit.\n")

        choice = input("Enter your choice: ")

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

                print("Invalid choice")


if __name__ == "__main__":          #! It mean if our file have an method name main then run it without asking anything to user.

    main()