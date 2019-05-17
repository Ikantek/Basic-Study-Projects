#pragma once
#include <iostream>
#include <string>
#include <regex>
#include <vector>

class Check{
public:
    void check_operators();
    Check()
    {
        get_equation_from_user(equation);
    }
private:
    std::string equation;
    void get_equation_from_user(std::string &equation);


};

// FUNCTIONS_H
