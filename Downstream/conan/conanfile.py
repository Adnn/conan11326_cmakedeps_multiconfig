from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy


class DownstreamRecipe(ConanFile):
    name = "downstream"
    version = "1.0.0"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    generators = "CMakeToolchain", "CMakeDeps"

    requires = "internal/1.0.0@adnn"
    build_requires = "cmake/3.27.7"


    def layout(self):
        # Otherwise, root is the subfolder containing conanfile.py
        self.folders.root = ".."
        # Dedicated build folder per compiler
        compiler = str(self.settings.compiler)
        cmake_layout(self, build_folder=f"build-conan-{compiler}{self.settings.get_safe('compiler.version')}")


    def generate(self):
        ## Equivalent to generators = "CMakeToolchain"
        #tc = CMakeToolchain(self)
        #tc.generate()
        pass


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()


    def package(self):
        cmake = CMake(self)
        cmake.install()
