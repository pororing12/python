print("%d" % 123)
print("%5d" % 123)
print("%05d"% 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "python")
print("%10s" % "python")

print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))

##밑에거와 같음 boolvar, intVar, floatVar, strVar = True, 0, 0.0, "cook"
boolVar = True
intVar = 0
floatVar = 0.0
strVar = "cook"
print(type(boolVar))

var1 = var2 = var3 = var4 = 100
print("%d, %d %d %d" % (var1, var2, var3, var4))
print(bin(11), bin(0o11), bin(0x11), "\n",
      oct(11), "\t", oct(0b11), "\t", oct(0x11), "\n",
      hex(11), "\t", hex(0b11), "\t", hex(0o11))

