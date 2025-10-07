import RPi.GPIO as GPIO
dac_pin=[12]
dynamic_range=3.29
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    def set_voltage(self,voltage):
        if not(0.0 <= voltage <= 3.29):
            print(f"Напряжение выходит за динамический диапозон ЦАП (0.00 - {3.29:.2f} В)")
            print("Устанавливаем 0.0 В")
            return 0
        pwm=GPIO.PWM(12,200)
        pwm.start(0)
        norm=voltage/3.3
        pwm.ChangeDutyCycle(norm*100)
if __name__=="__main__":
    try:
        dac=PWM_DAC([12], 3.29, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не числою Попробуйте еще раз\n")
    finally:
        dac.deinit()

