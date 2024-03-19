import numpy as np

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        # Input to hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        # Activation function for hidden layer
        self.hidden_output = self.sigmoid(self.hidden_input)
        # Hidden to output layer
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        # Activation function for output layer
        self.output = self.sigmoid(self.output)
        return self.output
    
    def backward(self, X, y, output, learning_rate):
        # Compute gradients
        d_output = output - y
        d_hidden_output = np.dot(d_output, self.weights_hidden_output.T) * self.sigmoid_derivative(self.hidden_output)
        # Update weights and biases
        self.weights_hidden_output -= learning_rate * np.dot(self.hidden_output.T, d_output)
        self.bias_output -= learning_rate * np.sum(d_output, axis=0, keepdims=True)
        self.weights_input_hidden -= learning_rate * np.dot(X.T, d_hidden_output)
        self.bias_hidden -= learning_rate * np.sum(d_hidden_output, axis=0, keepdims=True)
        
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output, learning_rate)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}: loss {loss}")

# Example usage
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

model = FeedForwardNN(input_size=2, hidden_size=4, output_size=1)
model.train(X, y, epochs=10000, learning_rate=0.1)

# Test the trained model
output = model.forward(X)
print("Output after training:")
print(output)
