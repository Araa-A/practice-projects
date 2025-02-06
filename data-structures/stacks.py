#%% Task One

stack = []
lastbook = ""
stack.append("Harry Potter and the Sorcerer's Stone")
print(stack)
lastbook = stack.pop() # The popped item is now in the variable lastbook
print(lastbook)

# Add your code here
stack.append("Alice's Adventures in Wonderland")
stack.append("Percy Jackson & the Olympians")
stack.append("Matilda")

print(stack)
lastbook = stack.pop()
lastbook = stack.pop()

print(stack)

stack.append("The Lord of The Rings")
print(stack)

