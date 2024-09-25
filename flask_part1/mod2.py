import mod1     # here we are importing the mod1 but __name__ in the mod1 not acting like a main. Because its not its scope
print(f"Hello Girls- ({__name__})")

# Hence the if __name__ == "__main__" is used to secure the app from running because sometime i just want some class or functionality from the app 
# But i dont want to run the app. 