import module_b

def do_stuff():
    final_result = module-b.run_helper("default_options")
    if final_result:
        print("module_a, do_stuff completed successfully!")
    else:
        print("module_a, error calculating result!")

