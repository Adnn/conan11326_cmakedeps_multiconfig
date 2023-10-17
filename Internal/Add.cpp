#include "Add.h"

namespace ad {

    int add(int a, int b)
    {
        return a + b;
    }

    std::string getBuildType()
    {
#if defined(NDEBUG)
        return "Release (not debug)";
#else
        return "Debug";
#endif
    }

}

