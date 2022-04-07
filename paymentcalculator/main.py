import sys
from context.paymentcalculator import PaymentCalculatorContext
from exceptions import InvalidInputFormatError, InvalidHourRangeError
from facade.paymentcalculator import PaymentCalculatorFacade


def main(argv):
    try:
        with open(argv[1], "r") as f:
            PaymentCalculatorFacade(PaymentCalculatorContext(f.read())).execute()
    except InvalidInputFormatError as e:
        print(e)
        print(
            ''' Input file format must be as follows:
            One entry per line: '[EMPLOYEE_NAME]=[SCHEDULE]' where SCHEDULE
            consists of one or more comma separated entries: [MO|TU|WE|TH|FR|SA|SU]HH:00-HH:00
            Example: ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
                     RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
            '''
        )
    except InvalidHourRangeError as e:
        print(e)
        print("End hour must be greater than start hour.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(sys.argv)
