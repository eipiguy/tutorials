#files to compile
OBJS = 01_hello_SDL.cpp

#compiler used
CC = g++

#compilation options
# -w suppresses all warnings
COMPILER_FLAGS = -w

#libraries to link
LINKER_FLAGS = -lSDL2

#name of the resulting executable
OBJ_NAME = 01_hello_SDL

#compiles the executable
all : $(OBJS)
	$(CC) $(OBJS) $(COMPILER_FLAGS) $(LINKER_FLAGS) -o $(OBJ_NAME)
