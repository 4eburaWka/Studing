from os import system

from prettytable import PrettyTable


class PCComponent:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @classmethod
    def create(cls, inputs=None):
        if inputs is None:
            inputs = {} 
            for key in cls.__init__.__code__.co_varnames[1:]:
                value = input(f"Введите значение для {key}: ")
                if value.isdigit():
                    value = int(value)
                inputs[key] = value

        new_component = cls(**inputs)
        cls.objects.append(new_component)
        return new_component
    
    @classmethod
    def show_objects(cls):
        table = PrettyTable()
        table.field_names = ['№', *cls.__init__.__code__.co_varnames[1:]]
        for i, object in enumerate(cls.objects, start=0):
            table.add_row([i, *object.__dict__.values()])
        print(table)
    
    def show(self):
        for characteristic in self.__init__.__code__.co_varnames[1:]:
            print(self.__dict__[f"_{self.__class__.__name__}__{characteristic}"])
    
    @classmethod
    def create_from_file(cls, filename):
        with open(filename, 'r') as file:
            while True:
                inputs = {}
                for key in cls.__init__.__code__.co_varnames[1:]:
                    if not (value := file.readline()):
                        return
                    value = value[:-1]
                    if value.isdigit():
                        value = int(value)
                    inputs[key] = value
                cls.create(inputs)
                file.readline()


class CPU(PCComponent):
    objects = []
    def __init__(self, socket, company_name, cores_count, base_frequency, turbo_frequency, TDP) -> None:
        self.__socket = socket
        self.__company_name: str = company_name
        self.__cores_count: int = cores_count
        self.__base_frequency: int = base_frequency
        self.__turbo_frequency: int = turbo_frequency
        self.__TDP: int = TDP
    
    def get_data(self):
        return self.__socket, self.__company_name, self.__cores_count, self.__base_frequency, self.__turbo_frequency, self.__TDP


class Motherboard(PCComponent):
    objects = []
    def __init__(self, socket, company_name, form_factor, PCIExpressx16_count, PCIExpressx1_count, sata_count, CPUVideo_support, TDP) -> None:
        self.__socket: str = socket
        self.__company_name: str = company_name
        self.__form_factor: str = form_factor
        self.__PCIExpressx16_count: int = PCIExpressx16_count
        self.__PCIExpressx1_count: int = PCIExpressx1_count
        self.__sata_count: int = sata_count
        self.__CPUVideo_support: bool = CPUVideo_support
        self.__TDP: int = TDP

    def get_data(self):
        return self.__socket, self.__company_name, self.__form_factor, self.__PCIExpressx16_count, self.__PCIExpressx1_count, self.__sata_count, self.__CPUVideo_support, self.__TDP


class RAM(PCComponent):
    objects = []
    def __init__(self, company_name: str, memory_size: int, frequency: int):
        self.__company_name = company_name
        self.__memory_size = memory_size
        self.__frequency = frequency
    
    def get_data(self):
        return self.__company_name, self.__memory_size, self.__frequency


class Cooler(PCComponent):
    objects = []
    def __init__(self, company_name, supported_sockets, max_TDP) -> None:
        self.__company_name: str = company_name
        self.__supported_sockets: list = supported_sockets
        self.__max_TDP = max_TDP
    
    def get_data(self):
        return self.__company_name, self.__supported_sockets, self.__max_TDP


class GPU(PCComponent):
    objects = []
    def __init__(self, GPU_name: str, GPU_frequency: int, cores_count: int, RTX: bool, company_name: str, memory_frequency: int, TDP: int) -> None:
        self.__GPU_name = GPU_name
        self.__GPU_frequency = GPU_frequency
        self.__cores_count = cores_count
        self.__RTX = RTX
        self.__company_name = company_name
        self.__memory_frequency = memory_frequency
        self.__TDP = TDP
    
    def get_data(self):
        return self.__GPU_name, self.__GPU_frequency, self.__cores_count, self.__RTX, self.__company_name, self.__memory_frequency, self.__TDP
    

class SSD(PCComponent):
    objects = []
    def __init__(self, company_name: str, memory: int, speed: int) -> None:
        self.__company_name = company_name
        self.__memory = memory
        self.__speed = speed
    
    def get_data(self):
        return self.__company_name, self.__memory, self.__speed
    

class PowerBlock(PCComponent):
    objects = []
    def __init__(self, company_name: str, max_power: int) -> None:
        self.__company_name = company_name
        self.__max_power = max_power

    def get_data(self):
        return self.__company_name, self.__max_power


class PC:
    objects = []

    def __init__(self, CPU: CPU, Motherboard: Motherboard, RAM: RAM, Cooler: Cooler, GPU: GPU, SSD: SSD, PowerBlock: PowerBlock) -> None:
        self.__CPU = CPU
        self.__Motherboard = Motherboard
        self.__RAM = RAM
        self.__Cooler = Cooler
        self.__GPU = GPU
        self.__SSD = SSD
        self.__PowerBlock = PowerBlock
        PC.objects.append(self)

    @classmethod
    def create(cls):
        components = []
        for component in (CPU, Motherboard, RAM, Cooler, GPU, SSD, PowerBlock):
            component.show_objects()
            component_number = int(input('> '))
            try:
                components.append(component.objects[component_number])
            except IndexError:
                component.create()
        return PC(*components)
    
    @classmethod
    def find_the_best(cls):
        print("Выберите компонент")
        component_num = int(input(
"""1. Процессор.
2. Материнская плата.
3. Оперативная память.
4. Кулер.
5. Видеокарта.
6. SSD.
7. Блок питания.
> """
        ))
        component_name = ("CPU", "Motherboard", "RAM", "Cooler", "GPU", "SSD", "PowerBlock")[component_num-1]
        component = (CPU, Motherboard, RAM, Cooler, GPU, SSD, PowerBlock)[component_num-1]
        print("Выберите характеристику компонента")
        for i, characteristic in enumerate(component.__init__.__code__.co_varnames[1:], start=1):
            print(f"{i}. {characteristic}")
        characteristic = component.__init__.__code__.co_varnames[int(input("> "))]

        
        return max(PC.objects, key=lambda pc: pc.__dict__["_PC__"+component_name].__dict__[f"_{component_name}__"+characteristic])


def choose_component():
    while True:
        component = input(
"""1. Процессор.
2. Материнская плата.
3. Оперативная память.
4. Кулер.
5. Видеокарта.
6. SSD.
7. Блок питания.
> """
        )
        match(component):
            case '1':
                return CPU
            case '2':
                return Motherboard
            case '3':
                return RAM
            case '4':
                return Cooler
            case '5':
                return GPU
            case '6':
                return SSD
            case '7':
                return PowerBlock


if __name__ == '__main__':

    while True:
        menu = input(
"""1. Создать новый компонент.
2. Считать данные с файла.
3. Посмотреть компоненты.
4. Собрать компьютер.
5. Найти лучший компьютер по отдельной характеристике.
6. Выход.
> """
        )
        match(menu):
            case '1':
                choose_component().create()
            case '2':
                for component, name in zip((CPU, Motherboard, RAM, Cooler, GPU, SSD, PowerBlock), ("CPU", "Motherboard", "RAM", "Cooler", "GPU", "SSD", "PowerBlock")):
                    component.create_from_file(f"SSP\\lab1\\{name}.txt")
            case '3':
                choose_component().show_objects()
            case '4':
                PC.create()
            case '5':
                pc = PC.find_the_best()
                for component in pc.__init__.__code__.co_varnames[1:]:
                    print(component, end=': \n')
                    pc.__dict__[f"_PC__{component}"].show()
            case '6':
                break