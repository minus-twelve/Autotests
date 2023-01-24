package ru.deliveryClub;

import org.junit.Test;
import org.junit.Assert;
import org.openqa.selenium.chrome.ChromeDriver;

public class FirstTest {
    @Test
    public void firstTest() {
        System.setProperty("webdriver.chrome.driver", "C:/chromedriver.exe");
        ChromeDriver driver = new ChromeDriver();
        driver.get("https://www.delivery-club.ru");
        String title = driver.getTitle();
        Assert.assertTrue(title.equals("Быстрая доставка еды Delivery Club"));
        driver.quit();
    }


}
