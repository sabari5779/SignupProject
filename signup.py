def signup(username, password):
    if not username:
        return "Username is required"

    if len(password) < 6:
        return "Password must contain 6 characters"

    return "Signup successful!"

print(signup("student", "hello123"))