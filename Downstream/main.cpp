#include <iostream>

#include <internal/Add.h>


int main(int argc, char * argv[])
{
    std::cout << "I am MyApp, I can add 2 and 4: "
        << ad::add(2, 4)
        << ".\n"
        << " The library build type is: " << ad::getBuildType() << "."
        << std::endl;
    return 0;
}
