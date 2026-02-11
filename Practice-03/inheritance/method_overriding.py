class Logger:
    def log(self, msg):
        return f"[LOG] {msg}"

class FileLogger(Logger):
    def log(self, msg):
        base = super().log(msg)
        return base + " (saved to file)"

l1 = Logger()
l2 = FileLogger()

print(l1.log("Hello"))
print(l2.log("Hello"))
