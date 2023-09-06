import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center"
        }}>
          <p>
            <h1 className="hero__title">{siteConfig.title}</h1>
            <p className="hero__subtitle">{siteConfig.tagline}</p>
            <div className={styles.buttons}>
              <Link
                className="button button--secondary button--lg"
                to="/docs/intro">
                Getting started Tutorial - 5min ⏱️
              </Link>
            </div>
          </p>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main style={{
        padding: "1rem",
        marginRight: 15,
        marginLeft: 15
      }}>
        <div style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          alignContent: "center",
          justifyContent: "center"
        }}>

        </div>

        {/* <HomepageFeatures /> */}
        <h3 style={{
          marginTop: 10,
        }}>Installation</h3>
        <pre>
          pip3 install swibots
        </pre>
        <h3 style={{
          marginTop: "18px"
        }}>
          Installing from source
        </h3>
        <pre>
          pip3 install git+https://github.com/switchcollab/Switch-Bots-Python-Library.git
        </pre>
        <h3 style={{
          marginTop: 15
        }}>
          Say Hi 👋 to self!
        </h3>
        <pre>
          <code aria-multiline>
            async with BotApp(token) as bot:<br />
            {'    '}await bot.send_message(user_id=0,
            message="Hello 👋 from swibots!")
          </code>

        </pre>
      </main>
    </Layout>
  );
}
