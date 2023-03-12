import React from 'react';
import Article from '../../components/article/Article';
import { blog01, blog02, blog03, blog04, blog05 } from './imports';
import './blog.css';

const Blog = () => {
  return (
    <div className="gpt3__blog section__padding" id="blog">
    <div className="gpt3__blog-heading">
      <h1 className="gradient__text">We got you some interesting articles, <br /> Based on your device energy consumption.</h1>
    </div>
    <div className="gpt3__blog-container">
      <div className="gpt3__blog-container_groupA">
        <Article imgUrl={blog01} date="Sep 26, 2023" title=<a href='https://www.coolingindia.in/energy-conservation-ac-air-conditioner-energy-saving-tips-bee-guidelines-star-rating-magazine-news-article/' target='blank'>Energy Conservation for Air Conditioner.</a>/>
      </div>
      <div className="gpt3__blog-container_groupB">
        <Article imgUrl={blog02} date="Sep 26, 2023" title=<a href='https://www.electricaltechnology.org/2016/12/energy-efficient-lighting-techniques-to-implement-it.html' target='blank'>Why is energy efficient lighting important?</a>/>
        <Article imgUrl={blog03} date="Sep 26, 2023" title=<a href='https://www.myla.in/blog/how-to-use-geyser/#:~:text=How%20to%20reduce%20geyser%20electricity%20consumption%3F%201%20Avoid,Wondering%20how%20to%20set%20your%20geyser%20timer%3F%20' target='blank'>How to use geyser properly to reduce bill?</a>/>
        <Article imgUrl={blog04} date="Sep 26, 2023" title=<a href='https://www.deepakkumaryadav.in/2021/04/Energy%20Conservation%20Techniques%20In%20Fans%20And%20Electronics%20Regulators.html#:~:text=1%20Use%20electronic%20regulator%20in%20place%20of%20conventional,8%20Use%20windows%20to%20allow%20natural%20air%20circulations' target='blank'>Energy conservation techniques in fan and electronic regulators.</a>/>
        <Article imgUrl={blog05} date="Sep 26, 2023" title=<a href='https://electrical-engineering-portal.com/6-energy-efficiency-improvement-opportunities-in-fan-systems' target='blank'>Efficiency improvement opportunities in fan systems.</a>/>
      </div>
    </div>
  </div>
  )
}

export default Blog