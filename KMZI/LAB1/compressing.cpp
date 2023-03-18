#include <iostream>
#include <fstream>
#include <queue>
#include <unordered_map>
using namespace std;

// Definition of a node in the Huffman tree
struct Node {
    char c;
    int freq;
    Node* left;
    Node* right;

    Node(char c, int freq, Node* left = nullptr, Node* right = nullptr) {
        this->c = c;
        this->freq = freq;
        this->left = left;
        this->right = right;
    }

    ~Node() {
        if (left != nullptr) delete left;
        if (right != nullptr) delete right;
    }
};

// Build the Huffman tree based on the frequency table
Node* build_huffman_tree(const unordered_map<char, int>& freq_table) {
    // Build a priority queue of nodes
    auto cmp = [](Node* a, Node* b) { return a->freq > b->freq; };
    priority_queue<Node*, vector<Node*>, decltype(cmp)> pq(cmp);
    for (auto& p : freq_table) {
        pq.push(new Node(p.first, p.second));
    }

    // Build the Huffman tree
    while (pq.size() > 1) {
        Node* min1 = pq.top();
        pq.pop();
        Node* min2 = pq.top();
        pq.pop();
        Node* internal_node = new Node('\0', min1->freq + min2->freq, min1, min2);
        pq.push(internal_node);
    }

    // Return the root of the Huffman tree
    return pq.top();
}

void generate_huffman_codes_helper(Node* node, string& code, unordered_map<char, string>& huffman_codes) {
    if (node->left == nullptr && node->right == nullptr) {
        huffman_codes[node->c] = code;
        return;
    }
    code.push_back('0');
    generate_huffman_codes_helper(node->left, code, huffman_codes);
    code.pop_back();
    code.push_back('1');
    generate_huffman_codes_helper(node->right, code, huffman_codes);
    code.pop_back();
}

// Generate the Huffman codes for each symbol in the Huffman tree
unordered_map<char, string> generate_huffman_codes(Node* root) {
    unordered_map<char, string> huffman_codes;
    string code = "";
    generate_huffman_codes_helper(root, code, huffman_codes);
    return huffman_codes;
}

// Encode the input text using the Huffman codes
string encode(const string& text, const unordered_map<char, string>& huffman_codes) {
    string encoded_text = "";
    for (char c : text) {
        encoded_text += huffman_codes.at(c);
    }
    return encoded_text;
}

// Decode the encoded text using the Huffman tree
string decode(const string& encoded_text, Node* root) {
    string decoded_text = "";
    Node* node = root;
    for (char c : encoded_text) {
        if (c == '0') {
            node = node->left;
        } else if (c == '1') {
            node = node->right;
        }
        if (node->left == nullptr && node->right == nullptr) {
            decoded_text += node->c;
            node = root;
        }
    }
    return decoded_text;
}

int main() {
    // Read the input text
    string path, text;
    cout << "Введите имя файла: ";
    getline(cin, path);
    ifstream file(path);
    getline(file, text);
    file.close();

    // Compute the frequency table
    unordered_map<char, int> freq_table;
    for (char c : text) {
        freq_table[c]++;
    }

    // Build the Huffman tree and generate the Huffman codes
    Node* root = build_huffman_tree(freq_table);
    unordered_map<char, string> huffman_codes = generate_huffman_codes(root);

    // Encode the input text using the Huffman codes
    string encoded_text = encode(text, huffman_codes);

    // Divide the encoded text into groups of 8 characters, convert each group to a byte, and write the bytes to a file
    ofstream out(path + "_comp", ios::binary);
    char byte = 0;
    int bit_count = 0;
    for (char c : encoded_text) {
        byte <<= 1;
        if (c == '1') {
            byte |= 1;
        }
        bit_count++;
        if (bit_count == 8) {
            out.put(byte);
            byte = 0;
            bit_count = 0;
        }
    }
    if (bit_count > 0) {
        byte <<= (8 - bit_count);
        out.put(byte);
    }
    out.close();

    cout << "Encoded text: " << encoded_text << endl;

    // Read the encoded bytes from the file and convert them back to a string of 0s and 1s
    ifstream in(path + "_comp", ios::binary);
    string encoded_bytes = "";
    char byte_in;
    while (in.get(byte_in)) {
        for (int i = 7; i >= 0; i--) {
            encoded_bytes += ((byte_in >> i) & 1) ? "1" : "0";
        }
    }
    in.close();

    // Decode the encoded text using the Huffman tree
    string decoded_text = decode(encoded_bytes, root);
    cout << "Decoded text: " << decoded_text << endl;

    // Clean up the memory
    delete root;
}
