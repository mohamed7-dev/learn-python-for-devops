# For Loops

# they are of the same structure exists in any language

# Python For Loop abstract syntax is <for item in sequence>
# Where sequence can be list, tuple, string, range(num), ...etc

databases = ["database_1","database_2"]
for db in databases:
    print(db)

for num in range(10):
    print(num)    

# While Loops <The same one exists in any language>

count = 0
while count < 2:
    print(databases[count])
    count += 1

# Real App Example
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)