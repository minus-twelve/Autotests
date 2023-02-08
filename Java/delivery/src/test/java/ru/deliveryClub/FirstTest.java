package ru.deliveryClub;

import org.junit.Test;
import org.junit.Assert;


public class FirstTest extends WebDriverSettings {

    @Test
    public void firstTest() {
        driver.get("https://www.delivery-club.ru");
        String title = driver.getTitle();
        Assert.assertTrue(title.equals("Быстрая доставка еды Delivery Club"));
    }

    @Test
    public void secondTest() {
        driver.get("https://www.delivery-club.ru");
        String title = driver.getTitle();
        Assert.assertTrue(title.equals("Быстрая доставка еды Delivery Club"));
    }





}
