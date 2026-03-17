#ifndef RECTANGLE
#define RECTANGLE


class Rectangle{

    private:
    
        int width = 0;
        int height = 0;

    public:

        Rectangle(int width, int height);
        void draw();
        int getArea();
        int getWidth();
        void setWidth(int width);
        int getHight();
        void setHight(int height);
        
};      


#endif