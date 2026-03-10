#ifndef RECTANGLE
#define RECTANGLE


class Rectangle{

    private:
        int width;
        int height;

    public:
        void draw();
        int getArea();

        // Getter
        int getWidth();
        // Setter (Mutator)
        void setWidth(int width);

        int getHight();
        void setHight(int height);
};      


#endif