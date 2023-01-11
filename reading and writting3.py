def write(file, name, age, job):
    outfile = open(file,'w')
    outfile.write("Name:"+name+"\n")
    outfile.write("Age:"+str(age)+"\n")
    outfile.write("Job:"+job+"\n")
    outfile.close()
