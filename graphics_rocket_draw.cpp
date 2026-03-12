#include <GL/glut.h>
#include <math.h>

// Function to draw a circle
void drawCircle(float cx, float cy, float r) {
    glBegin(GL_POLYGON);
    for (int i = 0; i < 360; i += 10) {
        float theta = i * 3.14159f / 180.0f;
        glVertex2f(cx + r * cos(theta), cy + r * sin(theta));
    }
    glEnd();
}

// Function to draw  cloud
void drawCloud(float x, float y, float scale) {
    glColor3f(1.0f, 1.0f, 1.0f); // White color for clouds
    glPushMatrix();
    glTranslatef(x, y, 0);
    glScalef(scale, scale, 1.0f);

    drawCircle(0, 0, 30);
    drawCircle(35, 15, 40);
    drawCircle(75, 5, 35);
    drawCircle(105, -5, 25);
    drawCircle(40, -15, 30);

    glPopMatrix();
}

// Function to draw the rocket
void drawRocket() {
    glPushMatrix();

    // Position the rocket and tilt it
    glTranslatef(300.0f, 200.0f, 0.0f);
    glRotatef(-45.0f, 0.0f, 0.0f, 1.0f); // Rotate 45 degrees to point top-right

    // 1. Rocket Body (Dark Red / Maroon)
    glColor3f(0.5f, 0.0f, 0.05f);
    glBegin(GL_QUADS);
    glVertex2f(-40.0f, -60.0f);
    glVertex2f(40.0f, -60.0f);
    glVertex2f(40.0f, 60.0f);
    glVertex2f(-40.0f, 60.0f);
    glEnd();

    // 2. Rocket Nose (Bright Red)
    glColor3f(0.9f, 0.1f, 0.15f);
    glBegin(GL_TRIANGLES);
    glVertex2f(-40.0f, 60.0f);
    glVertex2f(40.0f, 60.0f);
    glVertex2f(0.0f, 130.0f); // Point of the nose
    glEnd();

    // 3. Engine Flames / Fins (Yellow)
    glColor3f(1.0f, 1.0f, 0.0f);
    glBegin(GL_TRIANGLES);

    // Left flame
    glVertex2f(-40.0f, -60.0f);
    glVertex2f(-10.0f, -60.0f);
    glVertex2f(-30.0f, -110.0f);

    // Right flame
    glVertex2f(10.0f, -60.0f);
    glVertex2f(40.0f, -60.0f);
    glVertex2f(30.0f, -110.0f);

    glEnd();

    glPopMatrix();
}


void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw top cloud
    drawCloud(250.0f, 480.0f, 1.2f);

    // Draw lower-left cloud
    drawCloud(100.0f, 350.0f, 1.5f);

    // Draw the rocket
    drawRocket();

    glFlush();
}


void init() {
    // Set background color to light sky blue
    glClearColor(0.6f, 0.82f, 0.92f, 1.0f);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // (Width: 800, Height: 600)
    gluOrtho2D(0.0, 800.0, 0.0, 600.0);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);


    glutInitWindowSize(800, 600);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("2D Rocket");

    init();


    glutDisplayFunc(display);


    glutMainLoop();

    return 0;
}
