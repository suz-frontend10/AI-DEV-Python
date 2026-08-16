import demo

print("Runner finished")

'''
Python is executing demo.py directly, so:
__name__ == "__main__"
But when runner.py does:
import demo
demo.py is being imported as a module, so:
__name__ == "demo"
'''