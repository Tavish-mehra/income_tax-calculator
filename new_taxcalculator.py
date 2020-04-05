import pygame
pygame.init()
    
class TAX():

    
    income_from_Salaries = int(input("Enter your income from  Salaries : "))
    income_from_House_Property = int(input("Enter your income from House_Property : "))
    income_from_Business = int(input("Enter your income from Business: "))
    income_from_CapiTal_Gains = int(input("Enter your income from CapiTal Gains : "))
    income_from_any_other_sources = int(input("Enter your income from any other sources : "))
    print()
    gross_total_income = (income_from_Salaries + income_from_House_Property + income_from_Business + income_from_CapiTal_Gains + income_from_any_other_sources)
    print("Your Gross Total Income is",gross_total_income)

    Deduction = int(input("Enter Your Total Deduction: "))

    Taxable_Income = (gross_total_income - Deduction)


    def Logic_calculations(self):

        if self.Deduction <= 150000:
            print()
            print("Your Taxable Income is",self.Taxable_Income)
        else:
            print("Deduction should be les than or equal to 150000")


        if self.Taxable_Income <= 250000:
            self.income_tax = (((self.Taxable_Income - 250000)*0) - 12500)

        elif 250000 < self.Taxable_Income <= 500000:
            self.income_tax = (((self.Taxable_Income - 250000) *0.05) - 12500)


        elif 500000 < self.Taxable_Income <= 750000:
            self.income_tax = ((500000 - 250000)*(0.05)) + ((self.Taxable_Income - 500000)*(0.1))

        elif 750000 < self.Taxable_Income <= 1000000:
            self.income_tax = ((500000 - 250000)*(0.05)) + ((750000 - 500000)*(0.1)) + ((self.Taxable_Income - 750000)*0.15)

        elif 1000000 <self.Taxable_Income <= 1250000:
            self.income_tax = ((500000 - 250000)*(0.05)) + ((750000 - 500000)*(0.1)) + ((1000000 - 750000)*0.15) + ((self.Taxable_Income - 1000000)*0.2)

        elif 1250000 < self.Taxable_Income <=1500000:
            self.income_tax = ((500000 - 250000)*(0.05)) + ((750000 - 500000)*(0.1)) + ((1250000 - 1000000) *0.15) + ((self.Taxable_Income - 1250000)*0.25)

        else: 
            self.income_tax = ((500000 - 250000)*(0.05)) + ((750000 - 500000)*(0.1)) + ((1250000 - 1000000) *0.15) + ((1250000 - 1000000)*0.25) + ((self.Taxable_Income - 1500000)*0.3)




        if self.income_tax < 0:
            self.income_tax = (self.income_tax*-1)*0
            
        else:
            self.income_tax = self.income_tax

        print(self.income_tax)
    

        # For displaying the income tax in the  pygame window.

        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Inncome Tax Calculator')
        font = pygame.font.SysFont('comicsans',40)
        text= font.render("Your Income Tax : Rs." + str(self.income_tax),1,(255,0,0))
        win.blit(text,(20, 250))
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    

TAX()
TAX().Logic_calculations()



# Tax Slabs
# 0 - 2.5l = nil
# 2.5 - 5l = 5%
# 5  - 10l = 20%
# over 10l = 30%
