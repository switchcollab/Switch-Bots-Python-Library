import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import CodeBlock from '@theme/CodeBlock';

import styles from './index.module.css';
import './custom.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}> 
          <Link
            className="button button--secondary button--lg"
            style={{ marginRight: '1rem' }}
            to="/docs/intro">
            Get Started in 5 Minutes ⏱️
          </Link>
          <Link
            className="button button--outline button--lg button--secondary"
            to="https://github.com/switchcollab/Switch-Bots-Python-Library"
            target="_blank"
            rel="noopener noreferrer">
            View on GitHub
          </Link>
        </div>
      </div>
    </header>
  );
}

function Feature({ title, description, icon }) {
  return (
    <div className={clsx('col col--4', styles.feature)}>
      <div className="text--center">
        <i className={`fas ${icon} ${styles.featureIcon}`}></i>
      </div>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function CodeExample({ title, code }) {
  return (
    <div className={clsx('col col--6', styles.codeExample, 'margin-bottom--lg')}>
      <h3>{title}</h3>
      <CodeBlock language="python">{code}</CodeBlock>
    </div>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="SwiBots - A powerful Python library for building Switch app bots">
      <HomepageHeader />
      <main>
        <section className={clsx(styles.features, 'features')}>
          <div className="container">
            <div className="row">
              <Feature
                title="Easy to Use"
                description="SwiBots is designed with simplicity in mind. Get your bot up and running on the Switch platform in just a few lines of code."
                icon="fa-rocket"
              />
              <Feature
                title="Powerful Features"
                description="From simple message handling to complex bot interactions, SwiBots provides a comprehensive toolkit for the Switch platform."
                icon="fa-cogs"
              />
              <Feature
                title="Extensible"
                description="Build custom plugins, extend functionality, and create advanced bots for the Switch platform with ease."
                icon="fa-puzzle-piece"
              />
            </div>
          </div>
        </section>
        <section className={clsx(styles.examples, 'examples')}>
          <div className="container">
            <h2>SwiBots in Action</h2>
            <div className="row">
              <CodeExample
                title="Sending Buttons"
                code={`from swibots import InlineMarkup, InlineKeyboardButton

await bot.send_message(
    message="Hi",
    user_id=bot.user.id,
    inline_markup=InlineMarkup([[
        InlineKeyboardButton("Click Me", url="https://example.com")
    ]])
)
`}
              />
              <CodeExample
                title="Sending Media"
                code={`await bot.send_media(
    message="This is a message",
    user_id=100,
    document="file.pdf",
    description="file_name.png",
    thumb="file.png"
)
`}
              />
            </div>
            <div className="row">
              <CodeExample
                title="Embedded Messages"
                code={`from swibots import EmbeddedMedia, EmbedInlineField

await bot.send_message(
    message="Embedded message",
    user_id=400,
    media=EmbeddedMedia(
        thumbnail="thumb_path.png",
        title="Embedded message.",
        header_name="Message from SwiBots!",
        header_icon="https://header.png",
        footer_title="Hello from the bot.",
        footer_icon="https://footer.png",
        inline_fields=[
            [
                EmbedInlineField("https://icon.png", "Nice Meeting You", "Hello 👋")
            ]
        ]
    )
)
`}
              />
              <CodeExample
                title="Handling Callbacks"
                code={`from swibots import CallbackQueryEvent, BotContext
from swibots import regexp, InlineMarkup, InlineKeyboardButton

@bot.on_callback_query(regexp("clb$"))
async def onCallback(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.answer(
        "Hello, this is a callback answer",
        show_alert=True
    )
`}
              />
            </div>
          </div>
        </section>
        <section className={clsx(styles.gettingStarted, 'gettingStarted')} style={{ marginTop: '4rem' }}>
          <div className="container" >
            <h2>Ready to dive in?</h2>
            <p>Explore our comprehensive documentation and start building amazing bots for the Switch platform today!</p>
            <div className={styles.buttons}>
              <Link
                className="button button--primary button--lg"
                to="/docs/intro">
                Explore Docs
              </Link>
              <Link
                className="button button--secondary button--lg"
                style={{ marginLeft: '1rem' }}
                to="/docs/examples/echo-bot">
                Create Your First Bot
              </Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
