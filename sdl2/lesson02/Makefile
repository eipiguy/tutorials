#files to compile
OBJS = 02_getting_an_image_on_the_screen.cpp

#compiler used
CC = g++

#compilation options
# -w suppresses all warnings
COMPILER_FLAGS = -w -g

#libraries to link
LINKER_FLAGS = -lSDL2

#name of the resulting executable
OBJ_NAME = 02_getting_an_image_on_the_screen

#compiles the executable
all : $(OBJS)
	$(CC) $(OBJS) $(COMPILER_FLAGS) $(LINKER_FLAGS) -o $(OBJ_NAME)
