#include "functions.h"
void Check::get_equation_from_user(std::string &equation){
    std::cout << "Please write the equation:" <<std::endl;
    std::cin >> equation;
}
void Check::check_operators(){
    std::string output_string;
    std::string available_sign ="0123456789abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ+-/*^%(){}[].=";
    for (size_t i=0; i<equation.length();i++){
        for (size_t j=0; j<available_sign.length();j++){
            if (equation[i]==available_sign[j]) break;
            else{
                if (j==available_sign.length()-1) {std::cout << "Wrong equation1" <<std::endl; exit(1);}
            }
        }
    }
    std::regex asd("([1-9]+[0-9]*[0-9]*[0-9]*(*){1,2})*([1-9]+[0-9]*[0-9]*[0-9]*)");
    std::regex operators(".*[\\-*+%^({\\[][\\-*+%^)}\\]].*"); //making sure that two operators or two specific brackets won't be next to each other
    std::regex at_leastone(".*[^=\\-*+%^]{1}=[^=\\-*+%^]{1}.*"); //making sure that we will have not a operator between "=" operator
    std::regex brac_corectness_left(".*[^{(\\[\\-*+/%^=][({\\[].*"); //not a oparetor after opening bracket
    std::regex brac_corectness_right(".*[)}\\]][^})\\]\\-*+/%^=].*"); //not a operator before closing bracket
    /*std::regex var_after_var(".*[a-zA-Z][a-zA-Z0-9].*");
    std::regex letter_after_num(".*[0-9][a-zA-Z]");
    |(std::regex_match(equation,var_after_var))||(std::regex_match(equation,letter_after_num))
    - if we would like to work only on numbers or variables created by one letter*/
    if (std::regex_match(equation,operators)  || !std::regex_match(equation,at_leastone) || std::regex_match(equation,brac_corectness_left) || std::regex_match(equation,brac_corectness_right) ){
        std::cout <<"Wrong equation2" <<std::endl;
        exit(1);
    }
    std::vector <char> left={'(','{','['};
    std::vector <char> right={')','}',']'};
    std::vector <char> bracket;
    for (size_t i=0; i<equation.length();i++){
        if (equation[i]=='='){
            if (bracket.size()!=0){
                std::cout <<"Wrong equation6" <<std::endl;
                exit(1);
            }
        }
        for (size_t j=0; j<left.size();j++){
            if (equation[i]==left[j]) bracket.insert(bracket.end(),left[j]);
            if (equation[i]==right[j]){
                if (bracket.size()!=0){
                    if (bracket[bracket.size()-1]==left[j]){
                        bracket.pop_back();
                    }
                    else{
                        std::cout <<"Wrong equation3" <<std::endl;
                        exit(1);
                    }
                }
                else{
                    std::cout <<"Wrong equation4" <<std::endl;
                    exit(1);
                }
            }
        }
    }
    if (bracket.size()!=0){
        std::cout <<"Wrong equation5" <<std::endl;
        exit(1);
    }
    std::cout<<"Correct equation"<<std::endl;

}
