def magic_string():
    magic_string.iteration = getattr(magic_string, 'iteration', 0)
    magic_string.iteration += 1
    return ("BestSchool, " * (magic_string.iteration - 1) + "BestSchool")
