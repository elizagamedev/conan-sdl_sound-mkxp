from conans import ConanFile, CMake, tools
import os.path


class SDLSoundMkxpConan(ConanFile):
    name = "sdl_sound-mkxp"
    version = "1.0.1"
    license = "GNU LGPLv2"
    url = "http://github.com/elizagamedev/conan-sdl_sound-mkxp"
    description = "Sound file format library for SDL"
    settings = "os", "compiler", "build_type", "arch"
    features = (
        "voc",
        "wav",
        "raw",
        "aiff",
        "au",
        "shn",
        "midi",
        "mpg123",
        "mikmod",
        "modplug",
        "ogg",
        "flac",
        "speex",
        "physfs",
    )
    options = dict({
        "shared": [True, False],
        "fPIC": [True, False],
    }, **{"with_{}".format(feature): [True, False] for feature in features})
    default_options = (
        "shared=False",
        "fPIC=False",
        "with_voc=True",
        "with_wav=True",
        "with_raw=True",
        "with_aiff=True",
        "with_au=True",
        "with_shn=True",
        "with_midi=True",
        "with_mpg123=True",
        "with_mikmod=False",
        "with_modplug=False",
        "with_ogg=True",
        "with_flac=True",
        "with_speex=False",
        "with_physfs=True",
    )
    requires = "sdl2/2.0.8@bincrafters/stable"
    generators = "cmake"
    exports_sources = "*"

    def config_options(self):
        del self.settings.compiler.libcxx
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        if self.options.with_ogg or self.options.with_flac or self.options.with_speex:
            self.requires("ogg/1.3.3@bincrafters/stable")
        if self.options.with_flac:
            self.requires("flac/1.3.2@bincrafters/stable")
        if self.options.with_ogg:
            self.requires("vorbis/1.3.6@bincrafters/stable")
        if self.options.with_physfs:
            self.requires("physfs/3.0.1@eliza/stable")

    def source(self):
        self.run("git clone https://github.com/Ancurio/SDL_sound.git")

    def build(self):
        cmake = CMake(self)
        for feature in self.features:
            enabled = getattr(self.options, "with_" + feature)
            cmake.definitions["ENABLE_" + feature.upper()] = enabled
        if not self.options["flac"].shared:
            cmake.definitions["STATIC_FLAC"] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
