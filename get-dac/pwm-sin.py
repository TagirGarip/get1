import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3
signal_frequency = 10
sampling_frequency = 100

if __name__ == "__main__":
    try:
        pwm = pwm.PWM_DAC(12, signal_frequency, 3.0, True)
        start = time.time()
        while True:
            finish = time.time() - start
            pwm.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, finish))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        pwm.deinit()