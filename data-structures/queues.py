#%% Task One

# Define the queue and the list of names
queue = []

def enqueue(name):
    queue.append(name)
    print(f"Enqueued: {name}")
    print(f"Queue state: {queue}")

def dequeue():
    if queue:
        removed_element = queue.pop(0)
        print(f"Dequeued: {removed_element}")
    else:
        print("Queue underflow! No items to dequeue.")
    print(f"Queue state: {queue}")

enqueue("Alice")
# Your code here
enqueue("Nia")
enqueue("Yuki")
enqueue("Carlos")

dequeue()

enqueue("Laila")
enqueue("Anwar")

dequeue()
dequeue()

#%% Task Two

popular_songs = [
    "Happy - Pharrell Williams",
    "Let It Go - Idina Menzel (from Frozen)",
    "Can't Stop the Feeling! - Justin Timberlake",
    "Shake It Off - Taylor Swift",
    "Uptown Funk - Mark Ronson ft. Bruno Mars",
    "Roar - Katy Perry",
    "Firework - Katy Perry",
    "Count on Me - Bruno Mars",
    "Best Day of My Life - American Authors",
    "A Thousand Years - Christina Perri",
    "I'm a Believer - The Monkees",
    "Three Little Birds - Bob Marley",
    "Here Comes the Sun - The Beatles",
    "Don't Worry, Be Happy - Bobby McFerrin",
    "Walking on Sunshine - Katrina and the Waves",
    "Wake Me Up Before You Go-Go - Wham!",
    "I Gotta Feeling - The Black Eyed Peas",
    "Viva La Vida - Coldplay",
    "Hey, Soul Sister - Train",
    "High Hopes - Panic! At The Disco",
    "Beautiful Day - U2",
    "Sugar - Maroon 5",
    "Perfect - Ed Sheeran",
    "Brave - Sara Bareilles",
    "Everything is Awesome - Tegan and Sara (from The LEGO Movie)",
]

# Write your code here




print("Next song:", popular_songs[0])
print("Song after that:",popular_songs[1])
print("Song after that:",popular_songs[2])
