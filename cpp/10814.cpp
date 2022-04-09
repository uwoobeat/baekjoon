#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

class Person {
    private:
        int order;
        int age;
        string name;
    public:
        Person(int _order, int _age, string _name);
        int get_order();
        int get_age();
        string get_name();
};

Person::Person(int _order, int _age, string _name) {
    order = _order;
    age = _age;
    name = _name;
}

int Person::get_order() {
    return order;
}

int Person::get_age() {
    return age;
}

string Person::get_name() {
    return name;
}

bool compare(Person p1, Person p2) {
    if (p1.get_age() == p2.get_age()) {
        return p1.get_order() < p2.get_order();
    } else return p1.get_age() < p2.get_age();
}

int main()
{
    FASTIO;
    int n; cin >> n;
    vector<Person> v;
    for(int i=0; i<n; i++) {
        int tmpAge; string tmpName;
        cin >> tmpAge >> tmpName;
        Person tmpPerson = Person(i, tmpAge, tmpName);
        v.push_back(tmpPerson);
    };

    sort(v.begin(), v.end(), compare);

    for(auto person : v) {
        cout << person.get_age() << ' ' << person.get_name() << '\n';
    }

    return 0;
}