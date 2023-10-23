#include <iostream>
using namespace std;
class Node
{
    public:
        int key;
        int val;
        Node *next = nullptr;
        Node(int key, int val)
        {
            this->key = key;
            this->val = val;
        }
        ~Node()
        {
            if (next)
                delete next;
        }
};
class LRUCache
{
    public:
        int cap;
        int size = 0;
        Node* head = nullptr;
        Node* tail = nullptr;

        LRUCache(int capacity)
        {
            if (capacity >0)
                this->cap = capacity;
            else
                this->cap = 1;
        }

        int get(int key)
        {
            Node* it = this->head;
            if (!it)
                return -1;
            if (it->key == key)
            {
                if (it->next)
                {
                    head = it->next;
                    it->next = nullptr;
                    tail->next = it;
                    tail = it;
                }
                return tail->val;       
            }
            while(it->next)
            {
                if (it->next->key == key)
                {
                    Node* target = it->next;
                    if(target->next)
                    {
                        it->next = target->next;
                        tail->next = target;
                        tail = target;
                    } 
                    return target->val;
                }
                it = it->next;
            }
            return -1;
        }

        void put(int key, int value)
        {
            if (this->size == this->cap == 1 && head->key != key)
            {
                delete head;
                delete tail;
                head = tail = new Node(key, value);
                return; 
            }
            if (!this->head)
            {
                this->head = this->tail = new Node(key, value);
                size++; 
                return;
            }
            if (this->get(key) != -1)
            {
                tail->val = value;
                return;
            }
            if (this->size == cap)
            {
                Node* currHead = head;
                head = currHead->next;
                currHead->next = nullptr;
                delete currHead;
                this->size--;
            }
            tail->next = new Node(key, value);
            tail = tail->next;
            this->size++;
        }
    };
int main()
{
    LRUCache cache(3);
    cout << cache.get(5) << endl;
    cache.put(5,3);
    cout << cache.get(5) << endl;
    cache.put(1,4);
    cout << cache.head->key << " " << cache.tail->key << endl;
    cache.put(2,7);
    cout << cache.head->key << " " << cache.tail->key << endl;

}
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */