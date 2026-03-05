#include <GL/glut.h>
#include <math.h>

// Helper function to draw circles cleanly
void drawCircle(float cx, float cy, float r) {
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < 30; i++) {
        float theta = 2.0f * 3.14159f * float(i) / 30.0f;
        float x = r * cos(theta);
        float y = r * sin(theta);
        glVertex2f(x + cx, y + cy);
    }
    glEnd();
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Set line color to black and thickness
    glColor3f(0.0f, 0.0f, 0.0f);
    glLineWidth(2.0f);

    // HEAD
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.16f, 0.52f);
        glVertex2f(0.16f, 0.52f);
        glVertex2f(0.16f, 0.80f);
        glVertex2f(-0.16f, 0.80f);
    glEnd();

    // MOUTH
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.04f, 0.58f);
        glVertex2f(0.04f, 0.58f);
        glVertex2f(0.04f, 0.60f);
        glVertex2f(-0.04f, 0.60f);
    glEnd();

    // NECK
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.06f, 0.44f);
        glVertex2f(0.06f, 0.44f);
        glVertex2f(0.06f, 0.52f);
        glVertex2f(-0.06f, 0.52f);
    glEnd();

    // TORSO
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.32f, -0.12f);
        glVertex2f(0.32f, -0.12f);
        glVertex2f(0.32f, 0.44f);
        glVertex2f(-0.32f, 0.44f);
    glEnd();

    // PELVIS / WAIST
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.24f, -0.40f);
        glVertex2f(0.24f, -0.40f);
        glVertex2f(0.24f, -0.12f);
        glVertex2f(-0.24f, -0.12f);
    glEnd();

    // LEFT ARM
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.32f, 0.36f);
        glVertex2f(-0.32f, -0.12f);
        glVertex2f(-0.64f, 0.00f);
    glEnd();

    // RIGHT ARM
    glBegin(GL_LINE_LOOP);
        glVertex2f(0.32f, 0.36f);
        glVertex2f(0.32f, -0.12f);
        glVertex2f(0.64f, 0.00f);
    glEnd();

    // LEFT HAND
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.64f, 0.00f);
        glVertex2f(-0.72f, -0.20f);
        glVertex2f(-0.56f, -0.20f);
    glEnd();

    // RIGHT HAND
    glBegin(GL_LINE_LOOP);
        glVertex2f(0.64f, 0.00f);
        glVertex2f(0.56f, -0.20f);
        glVertex2f(0.72f, -0.20f);
    glEnd();

    // LEFT LEG
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.14f, -0.40f);
        glVertex2f(-0.22f, -0.84f);
        glVertex2f(-0.06f, -0.84f);
    glEnd();

    // RIGHT LEG
    glBegin(GL_LINE_LOOP);
        glVertex2f(0.14f, -0.40f);
        glVertex2f(0.06f, -0.84f);
        glVertex2f(0.22f, -0.84f);
    glEnd();

    // LEFT FOOT
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.22f, -0.84f);
        glVertex2f(-0.26f, -0.98f);
        glVertex2f(-0.06f, -0.98f);
    glEnd();

    // RIGHT FOOT
    glBegin(GL_LINE_LOOP);
        glVertex2f(0.06f, -0.84f);
        glVertex2f(0.06f, -0.98f);
        glVertex2f(0.26f, -0.98f);
    glEnd();

    // EYES
    drawCircle(-0.06f, 0.70f, 0.03f); // LEFT EYE
    drawCircle(0.06f, 0.70f, 0.03f);  // RIGHT EYE

    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    // Window size and title
    glutInitWindowSize(450, 600);
    glutCreateWindow("plastic looking Robot");

    // White background
    glClearColor(1.0, 1.0, 1.0, 1.0);

    glutDisplayFunc(display);
    glutMainLoop();

    return 0;
}
