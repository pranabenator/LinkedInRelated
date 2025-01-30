import matplotlib.pyplot as plt
import matplotlib.patches as patches

class LogicCircuitSimulator:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.inputs = {
            'AND': [0, 0],
            'OR': [0, 0],
            'NOT': [0]
        }
        self.bulbs = {}
        self.initialize_diagram()

    def and_gate(self, a, b):
        return a & b

    def or_gate(self, a, b):
        return a | b

    def not_gate(self, a):
        return 1 if a == 0 else 0

    def draw_bulb(self, position, color, label):
        # Each bulb will have a text label for identification and color updates
        bulb = patches.Circle(position, 0.05, color=color, ec='black')
        self.ax.add_patch(bulb)
        self.bulbs[label] = bulb
        self.ax.text(position[0], position[1] - 0.1, label, ha='center', fontsize=8, style='italic')

    def toggle_input(self, event):
        if event.artist.get_gid():
            gate_type, idx = event.artist.get_gid().split('_')
            idx = int(idx)
            self.inputs[gate_type][idx] = 1 - self.inputs[gate_type][idx]
            event.artist.set_facecolor('yellow' if self.inputs[gate_type][idx] else 'lightgray')
            self.update_output(gate_type)

    def initialize_diagram(self):
        self.ax.axis('off')
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1.2)

        y_positions = [1, 0.8, 0.6]
        labels = ['AND', 'OR', 'NOT']
        colors = {0: 'lightgray', 1: 'yellow'}

        for i, gate_type in enumerate(labels):
            num_inputs = 2 if gate_type != 'NOT' else 1
            for j in range(num_inputs):
                inp_button = patches.Circle((0.1 + 0.2 * j, y_positions[i]), 0.05, color=colors[self.inputs[gate_type][j]], ec='black', picker=True, gid=f'{gate_type}_{j}')
                self.ax.add_patch(inp_button)
            self.draw_bulb((0.6, y_positions[i]), 'gray', gate_type)

        # Exit button
        exit_button = patches.Rectangle((0.4, 0.1), 0.2, 0.1, color='red', ec='black', picker=True, gid='exit')
        self.ax.add_patch(exit_button)
        self.ax.text(0.5, 0.15, 'Exit', ha='center', va='center', fontsize=12, color='white')

        self.fig.canvas.mpl_connect('pick_event', self.on_press)

    def update_output(self, gate_type):
        inputs = self.inputs[gate_type]
        if gate_type == 'AND':
            result = self.and_gate(inputs[0], inputs[1])
        elif gate_type == 'OR':
            result = self.or_gate(inputs[0], inputs[1])
        else:
            result = self.not_gate(inputs[0])
        self.bulbs[gate_type].set_color('yellow' if result else 'gray')

    def on_press(self, event):
        gid = event.artist.get_gid()
        if gid == 'exit':
            plt.close(self.fig)
        else:
            self.toggle_input(event)
        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()

if __name__ == "__main__":
    sim = LogicCircuitSimulator()
    sim.show()