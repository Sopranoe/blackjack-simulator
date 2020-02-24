class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber()
print("c2 = ComplexNumber()")
print((c2.real, c2.imag))
c2 = ComplexNumber(1,5)
print("c2 = ComplexNumber(1,5)")
print((c2.real, c2.imag))
c2 = ComplexNumber(3)
print("c2 = ComplexNumber(3)")
print((c2.real, c2.imag))
c2 = ComplexNumber(i=5)
print("c2 = ComplexNumber(i=5)")
print((c2.real, c2.imag))
c2 = ComplexNumber()
print("c2 = ComplexNumber(r=4, i=2)")
print((c2.real, c2.imag))