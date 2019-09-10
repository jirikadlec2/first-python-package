import module-b

def do_stuff():
    final_result = module-b.run_helper("default_options")
    if final_result:
        print("module-a, do_stuff completed successfully!")
    else:
        print("error calculating result!")

