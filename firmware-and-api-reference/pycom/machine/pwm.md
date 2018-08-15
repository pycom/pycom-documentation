# PWM

## class PWM – Pulse Width Modulation

### Quick Usage Example

```python
from machine import PWM
pwm = PWM(0, frequency=5000)  # use PWM timer 0, with a frequency of 5KHz
# create pwm channel on pin P12 with a duty cycle of 50%
pwm_c = pwm.channel(0, pin='P12', duty_cycle=0.5)
pwm_c.duty_cycle(0.3) # change the duty cycle to 30%
```

### Constructors

#### class machine.PWM\(timer, frequency\)

Create a PWM object. This sets up the `timer` to oscillate at the specified `frequency`. `timer` is an integer from 0 to 3. `frequency` is an integer from 1 Hz to 78 KHz \(this values can change in future upgrades\).

### Methods

#### pwm.channel\(id, pin \* , duty\_cycle=0.5\)

Connect a PWM channel to a pin, setting the initial duty cycle. `id` is an integer from 0 to 7. `pin` is a string argument. `duty_cycle` is a keyword-only float argument, with values between 0 and 1. Returns an instance of `PWMChannel`.

## class PWMChannel — PWM channel

### Methods

#### pwmchannel.duty\_cycle\(value\)

Set the duty cycle for a PWM channel. `value` is a float argument, with values between 0 and 1.

