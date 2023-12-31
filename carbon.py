
import matplotlib.pyplot as plt

class CarbonFootPrint:


    def __init__(self):

        self.name = input("Adınız nedir?")
        self.population = int(input("Evde yaşayan kaç kişi var?"))
        self.carbon_footprint = 0

        self.car_type_fp_val = {
            "dizel": 0.00269 * 22.2,
            "benzin": 0.00235 * 16.6,
            "lpg": 0.00188 * 11.36
        }

        self.milk_fp_val = {
            "sıklıkla": 10 * 12 * 2.8,
            "nadiren": 5 * 12 * 2.8,
            "hiç": 0 * 12
        }

        self.egg_fp_val = {
            "sıklıkla": 6 * 12 * 4.5,
            "nadiren": 3 * 12 * 4.5,
            "hiç": 0 * 12
        }

        self.red_meat_fp_val = {
            "sıklıkla": 10 * 12 * 34.6,
            "nadiren": 5 * 12 * 34.6,
            "hiç": 0 * 12
        }

        self.fish_meat_fp_val = {
            "sıklıkla": 10 * 12 * 5.1,
            "nadiren": 5 * 12 * 5.1,
            "hiç": 0 * 12
        }
    

    def calculate_electrical(self):

        kw = 0
        kw += float(input("Bir ayda ne kadar sıklıkla bulaşık makinesini kullanıyorsunuz?")) * 0.9
        kw += float(input("Bir ayda ne kadar sıklıkla kurutma makinesini kullanıyorsunuz?")) * 3    
        kw += float(input("Bir ayda ne kadar sıklıkla fön makinesini kullanıyorsunuz?")) * 1.25
        kw += float(input("Bir ayda ne kadar sıklıkla çamaşır makinesini kullanıyorsunuz?")) * 0.8
        kw += float(input("Bir ayda ne kadar sıklıkla tost makinesini kullanıyorsunuz?")) * 0.33
        kw += float(input("Bir ayda ne kadar sıklıkla kettle kullanıyorsunuz?")) * 0.16
        kw += float(input("Bir ayda ne kadar sıklıkla ütü kullanıyorsunuz?")) * 2

        electric_carbon_fp = (kw * 0.478) / self.population

        self.carbon_footprint += electric_carbon_fp

        return electric_carbon_fp
    

    def calculate_natural_gas(self):

        # ( doğal gaz kaynaklı kişi başı yıllık emisyon),
        # =Yıllık tüketilen doğal gaz miktarı*0,19/(evdeki kişi sayısı)
        avg_m3_tl_ratio = 6

        print("Belirtilen aylar için doğal gaz faturanızı yazınız.")
        natural_gas_bill = 0
        natural_gas_bill += float(input("Nisan: ")) * 4
        natural_gas_bill += float(input("Temmuz: ")) * 4
        natural_gas_bill += float(input("Eylül: ")) * 4
        natural_gas_bill += float(input("Ocak: ")) * 4

        natural_gas_carbon_fp = ((natural_gas_bill / avg_m3_tl_ratio) * 0.19) / self.population

        self.carbon_footprint += natural_gas_carbon_fp

        return natural_gas_carbon_fp
    

    def calculate_coal(self):

        # ( yakacak kaynaklı kişi başı yıllık emisyon) (kg/yıl)
        # = Kömür için tüketilen kömür miktarı*2/(evdeki kişi sayısı)

        coal_carbon_fp = float(input("Yıllık tükettiğiniz yakacak miktarı (kömür)")) * 2 / self.population
        self.carbon_footprint += coal_carbon_fp

        return coal_carbon_fp
    

    def calculate_car(self):
        
        # (araç kaynaklı kişi başı yıllık emisyon)
        # =Araba için=> otomobilin cinsi ve yakıt türüne göre hesaplanan miktar*kat edilen yol(km)
        car_type = input("Arabanız var mı? Yakıt türü nedir? (dizel benzin lpg)")

        avg_car_km = float(input("Yıllık ort kaç km yol yapıyorsunuz?"))
        car_carbon_fp = self.car_type_fp_val.get(car_type, 0) * avg_car_km

        self.carbon_footprint += car_carbon_fp

        return car_carbon_fp
    

    def calculate_motorcycle(self):
        
        # "Motorsikletiniz var mı? Yakıt türü nedir? (benzin ,elektrik) yıllık ort kaç km yol yapıyosunuz? (Motors kaynaklı k.b.y.e)"
        if input("Motorsikletiniz kullanıyor musunuz? (evet/hayır)") != 'evet':
            return 0
        
        motor_type = input("Yakıt türü nedir? (dizel benzin lpg)")

        avg_motor_km = float(input("Yıllık ort kaç km yol yapıyorsunuz?"))
        motor_carbon_fp = self.car_type_fp_val.get(motor_type, 0) * avg_motor_km

        self.carbon_footprint += motor_carbon_fp

        return motor_carbon_fp
    

    def calculate_public_transport(self):
        
        public_transport_carbon_fp = 0
        public_transport_carbon_fp += float(input("Bir yılda tren ile kaç km yol yapıyosunuz?")) * 0.11 # =Yapılan yol km *0,11
        public_transport_carbon_fp += float(input("Bir yılda otobüs ile kaç km yol yapıyosunuz?")) * 0.09            # =Yapılan km*0,09
        public_transport_carbon_fp += float(input("Bir yılda metro ile kaç km yol yapıyorsunuz?")) * 0.09         # =Yapılan km*0,09
        public_transport_carbon_fp += float(input("Bir yılda vapur ile kaç km yol yapıyosunuz?")) * 0.47          # Yapılan yol*0,47
        public_transport_carbon_fp += float(input("Bir yılda uçakla kaç uçuş yapıyorsunuz?")) * 2.52

        self.carbon_footprint += public_transport_carbon_fp

        return public_transport_carbon_fp
    

    def calculate_food(self):        

        # Eğer İkisinin de cevabı evetse +3000kg
        # Eğer ikisi de hayırsa+600kg
        # Biri evet biri hayırsa  +2000kg
        shopping = input("Sık sık alışveriş yapar mısınız? (evet/hayır)") == "evet"
        package_food = input("Paketli yiyecekler tüketir misiniz? (evet/hayır)") == "evet"

        food_carbon_fp = (3000 if shopping and package_food else (2000 if shopping or package_food else 600))
        food_carbon_fp += self.milk_fp_val.get(input("1 ayda hangi sıklıkla süt tüketiyorsunuz? (sıklıkla nadiren hiç)"), 0)
        food_carbon_fp += self.egg_fp_val.get(input("1 ayda hangi sıklıkla yumurta tüketiyorsunuz? (sıklıkla nadiren hiç)"), 0)
        food_carbon_fp += self.red_meat_fp_val.get(input("1 ayda hangi sıklıkla kırmızı et tüketiyorsunuz? (sıklıkla nadiren hiç)"), 0)
        food_carbon_fp += self.fish_meat_fp_val.get(input("1 ayda hangi sıklıkla balık et tüketiyorsunuz? (sıklıkla nadiren hiç)"), 0)

        self.carbon_footprint += food_carbon_fp

        return food_carbon_fp


    def calculate_cigar(self):

        cigar_carbon_fp = float(input("Haftada kaç paket sigara kullanıyorsunuz?")) * 20 * 0.014 * 48

        self.carbon_footprint += cigar_carbon_fp

        return cigar_carbon_fp
    

    def calculate_all(self):

        fig, ax = plt.subplots()

        keys = [
            'Elektrik',
            'Doğal Gaz',
            'Kömür ve Odun',
            'Araba',
            'Motosiklet',
            'Toplu Taşıma',
            'Yemek',
            'Sigara',
            'TOPLAM'
        ]
        
        counts = [
            self.calculate_electrical(),
            self.calculate_natural_gas(),
            self.calculate_coal(),
            self.calculate_car(),
            self.calculate_motorcycle(),
            self.calculate_public_transport(),
            self.calculate_food(),
            self.calculate_cigar(),
            self.carbon_footprint
        ]

        print(f'Toplam karbon ayakizi {self.carbon_footprint}kg')

        bar_labels = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:olive', 'tab:cyan']

        ax.bar(keys, counts, color=bar_labels)

        ax.set_ylabel('Karbon ayak izi (kg)')
        ax.set_title(f'{self.name} için karbon ayak izi tablosu')

        plt.show()
 
if __name__ == '__main__':
    
    CarbonFootPrint().calculate_all()
