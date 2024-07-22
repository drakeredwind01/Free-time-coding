if __name__ == '__main__':

Exception Details with traceback:
except Exception as e:
    print("Error:")
    traceback.print_exc()

f-strings for Clear Messages:
except ValueError as e:
    print(f"Error: {e}")