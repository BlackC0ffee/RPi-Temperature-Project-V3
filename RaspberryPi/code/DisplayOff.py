import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio

RESET_PIN = 15
DC_PIN = 16

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128)
led.clear_display()
led.display()